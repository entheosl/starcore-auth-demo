# STAR.CORE Terminal UI Recreation (Unofficial)

A frontend-only UI demo recreated from the **publicly rendered `/login` page** of staryuki.com. This is an independent study/recreation, not the original website, product, or authentication system.

**Source inspection:** the observed live page is Next.js/React; its login terminal is mounted by a separate Unity Auth launcher script. The publicly rendered opening screen shows an uplink/boot sequence, seven-character Data Access Card entry, fluorescent chartreuse (#d6ff00) overlays and a black/noise terminal canvas. The opening view is reproduced as closely as possible. The later command shell and authentication form are **simulated reinterpretations**, not a verified exact clone of the original source UI.

## Run

Open `index.html`, or start any local static server in this directory:

```sh
python3 -m http.server 8080
```

GitHub Pages can publish the project root directly. No npm, build system, API, database or backend.

## Interactive demo

1. Click `[ TRANSMIT ]`.
2. Enter card ID **`HATSUNE`**, hit Enter or Verify.
3. At the terminal, type `help`, `login`, or `register`.
4. Hardcoded login: ID **`operator`**, phrase **`starcore`**.
5. Demo registration accepts any appropriately formatted test email and a local form; simulated verification code: **`042623`**.

You may jump to `#access`, `#terminal`, `#login` or `#register` for QA.

**Safety:** Don't enter actual credentials. No entered form details or secrets are sent anywhere, stored in cookies, or persisted. The only external requests are optional Google Fonts. The page visibly identifies itself as an unofficial demo.

## Fidelity notes

- Opening screen typography, positions, colors, labels, and noise were developed from rendered site screenshots and HTML.
- Follow-on layouts are approximations, not extracted source code or verified UI screenshots.
- The original app rejects some narrow screens; this recreation instead provides responsive controls.