import rsa


def generateKeys():
    publicKey, privateKey = rsa.newkeys(512)

    file = open('asymmetric-public.pem', 'wb')
    file.write(publicKey._save_pkcs1_pem())
    file.close()
    file = open('asymmetric-private.pem', 'wb')
    file.write(privateKey._save_pkcs1_pem())
    file.close()


def encrypt():
    with open('asymmetric-public.pem', 'rb') as publicfile:
        keydata = publicfile.read()
    publicKey = rsa.PublicKey.load_pkcs1(keydata, 'PEM')

    with open('credentials.json') as jsonFile:
        data = jsonFile.read()
    message = data
    # message = 'daniel-searle'
    print(message)

    encMessage = rsa.encrypt(message.encode(),
                             publicKey)

    print("original string: ", message)
    print("encrypted string: ", encMessage)

    file = open('data.txt', 'wb')
    file.write(encMessage)
    file.close()


def decrypt():
    file = open('data.txt', 'rb')
    encryptedFile = bytes(file.read())

    with open('asymmetric-private.pem', 'rb') as privatefile:
        keydata = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(keydata, 'PEM')

    decMessage = rsa.decrypt(encryptedFile, privkey).decode()

    print("decrypted string using read from file: ", decMessage)


# generateKeys()
encrypt()
# decrypt()
