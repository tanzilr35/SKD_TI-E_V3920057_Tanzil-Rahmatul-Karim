# Algoritme Euklides yang diperluas untuk menemukan modular inverse
# Algoritme Euklides = suatu algoritme untuk menentukan faktor persekutuan terbesar dari dua bilangan bulat.
# contoh: modinv(7, 26) = 15
def egcd(a, b):
  x,y, u,v = 0,1, 1,0
  while a != 0:
    q, r = b//a, b%a
    m, n = x-u*q, y-v*q
    b,a, x,y, u,v = a,r, u,v, m,n
  gcd = b
  return gcd, x, y
 
def modinv(a, m):
  gcd, x, y = egcd(a, m)
  if gcd != 1:
    return None  # modular inverse tidak tersedia
  else:
    return x % m
 
# fungsi enkripsi
def affine_encrypt(text, key):
  # Rumus enkripsi affine
  '''
  C = (a*P + b) % 26 
  '''
  return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                + ord('A')) for t in text.upper().replace(' ', '') ])
 
 
# fungsi dekripsi
def affine_decrypt(cipher, key):
  # Rumus dekripsi affine
  '''
  P = (a^-1 * (C - b)) % 26
  '''
  return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                  % 26) + ord('A')) for c in cipher ])
 
# Hasil output dari fungsi di atas
def main():
  # masukkan teks dan kuncinya
  text = 'Tanzil Rahmatul Karim'
  key = [3, 5]
 
  # memanggil fungsi enkripsi
  affine_encrypted_text = affine_encrypt(text, key)
 
  # memunculkan plaintext
  print('Plaintext: {}'.format(text))

  # memunculkan kunci
  print('Kunci A & B: {}'.format(key))

  # memunculkan teks enkripsi
  print('Encrypted Text: {}'.format( affine_encrypted_text ))
 
  # memunculkan teks dekripsi dan memanggil fungsi dekripsi
  print('Decrypted Text: {}'.format
  ( affine_decrypt(affine_encrypted_text, key) ))
 
 
if __name__ == '__main__':
  main()