# Sabse easy process — Hindi

## 1. Project chalana

### Windows

`RUN_PROJECT_WINDOWS.bat` par double-click karo.

### Linux / Skills Network terminal

```bash
chmod +x RUN_PROJECT_LINUX_MAC.sh
./RUN_PROJECT_LINUX_MAC.sh
```

App khulega:

```text
http://127.0.0.1:8000/
```

Login:

```text
Reviewer: reviewer / Reviewer@123
Admin: root / Root@123
```

## 2. Saare cURL outputs automatically banana

Server band kar do, phir:

### Windows

`CREATE_ALL_LOCAL_EVIDENCE_WINDOWS.bat` par double-click karo.

### Linux

```bash
./CREATE_ALL_LOCAL_EVIDENCE_LINUX_MAC.sh
```

Real output `evidence` folder mein ban jayega.

## 3. GitHub upload

GitHub repository ke root par directly ye sab dikhna chahiye:

```text
.github
server
scripts
README.md
Dockerfile
entrypoint.sh
```

Project ko kisi extra folder ke andar upload mat karna. Isse GitHub Actions workflow automatically detect hoga.

## 4. GitHub Actions

Repository → Actions → Car Dealership CI → Run workflow.

Green run ke baad real log Task 23 mein paste karna.

## 5. Code Engine deployment

Skills Network mein Code Engine project create karo, Code Engine CLI kholo, project folder mein jao aur run karo:

```bash
./DEPLOY_CODE_ENGINE_FROM_LOCAL.sh cars-dealership
```

End mein real public URL milega aur `evidence/deploymentURL` mein save ho jayega.

## 6. Screenshots

Exact filenames aur pages ke liye `CAPTURE_SCREENSHOTS.md` kholo.
