#!C:\Users\LJC\AppData\Local\Programs\Python\Python38-32\python.exe
print("content-type:text,html; charset=UTF-8\n")

#positional formatting
print('to {}. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim apple veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. {} Duis aute irure dolor in {} reprehenderit apple computer in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui {} officia deserunt mollit anim id est laborum.'.format('egoing', 12, 'egoing', 'egoing'))

#Named placeholder
print('to {name}. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim apple veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. {age:d} Duis aute irure dolor in {name} reprehenderit apple computer in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui {name} officia deserunt mollit anim id est laborum.'.format(name='egoing', age=12))
