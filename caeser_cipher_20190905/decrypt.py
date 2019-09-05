from pre_treat_message import pre_treat_message

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt(message, key):

    message = pre_treat_message(message)

    decrypted_message = ''

    # assemble the plaintext message by decrypting the message one letter at a time
    for c in message:
        if c not in ALPHABET:
            decrypted_message += c
            continue

        # find the corresponding decrypted letter and append it to decrypted_message
        decrypted_message += ALPHABET[(ALPHABET.find(c)-key)%len(ALPHABET)]

    return decrypted_message


# do not modify this file beyond this point
MESSAGE_ONE = 'NY NX XYNQQ XSTBNSL'
MESSAGE_TWO = 'WLSYPH AI KS WPIHHMRK'
MESSAGE_THREE = 'G AYLLMR DGLB KW ZMMRQ'

print (decrypt(MESSAGE_ONE, 31))  # decrypt the message with a key of 5
print (decrypt(MESSAGE_TWO, 4))  # decrypt the message with a key of 4
print (decrypt(MESSAGE_THREE, -2))  # decrypt the message with a key of -2
