# Export the real GitHub Actions log for Task 23

After uploading this project **at the repository root**, open the repository's **Actions** tab. The workflow is named **Car Dealership CI**.

## Browser method

1. Open the successful green workflow run.
2. Open the job **Test and Build Django Application**.
3. Expand the steps so the executed step names and output are visible.
4. Copy the log text into `evidence/CICD` and into the Coursera text box.

## GitHub CLI method

```bash
gh auth login
gh run list --workflow "Car Dealership CI" --limit 1
gh run view RUN_ID --log > evidence/CICD
```

Do not submit a placeholder. The output must come from your own successful workflow run.
