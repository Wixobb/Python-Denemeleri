import re

while (True):
    password = input("Parolanızı giriniz: ") #input

    # burada çok yaygın şifreler ile aynı mı diye bakıyoruz.
    if password in ["qwerty", "111111", "şifre", "password", "123456789", "123456", "sifre", "guest", "abc123", "Password1"]:
        print("Parolanız çok yaygın veya sıralı rakamlar içeriyor. Değiştirmenizi şiddetle tavsiye ederim.")

    else:
        # Parolanın uzunluğunu kontrol et
        if len(password) < 8:
            print("Parolanız çok kısa. En az 8 karakter olmalıdır.")
        # Parolanın büyük harf, küçük harf, rakam ve özel karakter içerip içermediğini kontrol et
        elif not re.search("[A-Z]", password):
            print("Parolanız en az bir büyük harf içermelidir.")
        elif not re.search("[a-z]", password):
            print("Parolanız en az bir küçük harf içermelidir.")
        elif not re.search("[0-9]", password):
            print("Parolanız en az bir rakam içermelidir.")
        elif not re.search("[!@#$%^&*()_+-=]", password):
            print("Parolanız en az bir özel karakter içermelidir.")
        # Parolanın sıralı veya tekrarlı karakterler içerip içermediğini kontrol et
        elif re.search("(.)\\1\\1", password):
            print("Parolanız üç veya daha fazla tekrarlı karakter içermemelidir.")
        elif re.search("123|234|345|456|567|678|789|890", password):
            print("Parolanız sıralı rakamlar içermemelidir.")
        elif re.search("abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz", password.lower()):
            print("Parolanız sıralı harfler içermemelidir.")
        # Parolanın güçlü olduğunu belirt
        else:
            print("Parolanız güçlü. Yine de belirli periyotlarda parolalarınızı güncellemenizi tavsiye ederim.")
