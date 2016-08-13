from encryption.EncDES import EncDES

if __name__ == '__main__':
    key = "ngfjdbt4"
    print("Test for DES")
    obj = EncDES(key)
    obj.test("testEncriptionsFile")