# short circuiting

is_Friend = False
is_User = True

if is_Friend and is_User:
    print('best friends forever')
else:
    print('just friends')

if is_Friend or is_User:
    print('best friends forever')
else:
    print('just friends')