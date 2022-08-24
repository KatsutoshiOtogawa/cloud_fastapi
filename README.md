# azure_aaa


gcloud iam service-accounts add-iam-policy-binding "${SERVICE_ACCOUNT}" \
  --project="${PROJECT_ID}" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/${WORKLOAD_IDENTITY_POOL_ID}/attribute.repository/${GitHubユーザー名}/${リポジトリ名}"

```bash
pipenv shell

python3
```

## django秘密キー作成。

途中でkeyを変えると値を復元できなくなるので、
必ず同じ値を使い続けること。

```
pipenv run create_secret_key
```

