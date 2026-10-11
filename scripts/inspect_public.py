#!/usr/bin/env python3
"""Fetch only publicly served webpage resources for reference analysis."""
import os, re, sys, urllib.request, urllib.parse
from html.parser import HTMLParser

ROOT="https://staryuki.com"
OUT="reference-capture"
os.makedirs(OUT, exist_ok=True)
class Assets(HTMLParser):
    def __init__(self):
        super().__init__();self.items=[];self.tags={}
    def handle_starttag(self,tag,attrs):
        d=dict(attrs);self.tags[tag]=self.tags.get(tag,0)+1
        if tag in ("script","link","img","video","source"):
            p=d.get("src") or d.get("href")
            if p:self.items.append((tag,p,d.get("rel"),d.get("type")))
def fetch(url):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/135.0 Safari/537.36"})
    with urllib.request.urlopen(req,timeout=25) as r:
        return r.read(),r.status,r.headers.get("Content-Type","")
print("PROBE START",ROOT,flush=True)
for name,path in (("home","/"),("login","/login")):
    try:
        b,status,mime=fetch(ROOT+path)
        with open(f"{OUT}/{name}-response.html","wb") as o:o.write(b)
        s=b.decode("utf-8","replace")
        p=Assets();p.feed(s)
        print("PAGE",name,"STATUS",status,"MIME",mime,"BYTES",len(b),"TAGS",p.tags,flush=True)
        print("PAGE",name,"TITLE",re.findall(r"<title[^>]*>(.*?)</title>",s,re.I|re.S)[:2],flush=True)
        print("PAGE",name,"SOURCEHEAD",repr(s[:1400]),flush=True)
        print("ASSETS",name,repr(p.items[:80]),flush=True)
        print("TECH",name,{word:word.lower() in s.lower() for word in ("_next/static","__NEXT_DATA__","vite","react","vue","p5.js","three.js","marathon","auth","terminal","register")},flush=True)
        if name=="login":
            for index,(tag,asset,_,_) in enumerate(p.items):
                if tag not in ("script","link"):continue
                url=urllib.parse.urljoin(ROOT+path,asset)
                if not urllib.parse.urlsplit(url).netloc.endswith("staryuki.com"):continue
                try:
                    content,astatus,atype=fetch(url)
                    ext="js" if (".js" in asset) else "css" if ".css" in asset else "txt"
                    with open(f"{OUT}/asset-{index}.{ext}","wb") as o:o.write(content)
                    text=content.decode("utf-8","replace")
                    snippet=[]
                    for phrase in ("HATSUNE","SKIP","register","cyber","terminal","email","password","Login","Register","font-family","background"):
                        match=re.search(re.escape(phrase),text,re.I)
                        if match: snippet.append((phrase,text[max(0,match.start()-85):match.end()+125].replace("\n"," ")[:240]))
                    print("RESOURCE",url,"STATUS",astatus,"TYPE",atype,"SIZE",len(content),"HITS",repr(snippet[:12]),flush=True)
                except Exception as e:print("ASSET_ERROR",url,str(e),flush=True)
    except Exception as e: print("PAGE_ERROR",name,repr(e),flush=True)
