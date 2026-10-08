# API keys

Sign in to the [Global Access Platform](https://gap.tomorrownow.org/) with an account that has access to the datasets you need.

## Create a key

1. Open your profile menu and choose **API Keys**.
2. Select **Generate new**.
3. Enter a name, description and expiry date, then choose **Create**.
4. Copy the key immediately. The full key is shown only once.

Store the key in an environment variable or a secret store. Do not put it in a URL, shared notebook, screenshot or source repository.

## Use the key

The measurement API uses the `Token` authentication scheme:

```bash
export GAP_API_TOKEN='YOUR_API_KEY'
curl --fail-with-body \
  'https://gap.tomorrownow.org/api/v1/measurement/options/' \
  --header "Authorization: Token $GAP_API_TOKEN"
```

An API key authenticates your account; it does not grant access to additional products. If a valid key receives a permission error, ask the GAP administrator to check your dataset access.

## Replace or delete a key

The API key page lists each key's name, description, creation date and expiry. Generate a replacement before an existing key expires, update your applications, then delete the old key using its trash icon and confirm the deletion. Other keys remain available.

A deleted or expired key cannot be used for subsequent requests. If a key is exposed, delete it and issue a replacement.

[Make your first request](measurements/getting-started.md)
