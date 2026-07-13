from extract.salesforce_auth import get_access_token

token, instance = get_access_token()

print("Access Token:")
print(token)

print("\nInstance URL:")
print(instance)