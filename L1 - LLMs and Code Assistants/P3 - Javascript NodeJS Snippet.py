# Javascript/NodeJS Snippet
import secrets

def generate_uuid():
  """Generates a UUID using Python's secrets module."""
  return ''.join(secrets.token_hex(16))

# Example of usage
print(generate_uuid())
