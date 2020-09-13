'''
open and with
https://docs.python.org/3/library/functions.html#open
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
'''

# open without error handling and manual close
w_file = open("a_file.tmp", "w")
w_file.write("123")
w_file.close()

# handle errors and close with try except
try:
    r_file = open("a_file.tmp", "r")
    try:
        r_file.read()
        r_file.write("abc")
    finally:
        print("close file")
        r_file.close()
except Exception as e:
    print(f"Exception: {e}")

# handle errors and close with context manager (no need to close)
try:
    with open('somefile.tmp', 'r') as r:
        print(r.read())
except FileNotFoundError:
    print("file not found")

# handle errors and open multiple files with context manager (no need to close)
try:
    with open('abc.tmp', 'w') as f, open("abc.tmp", "r") as r:
        f.write("abc")
        f.flush()
        print(r.read())
except Exception as e:
    print(f"Exception: {e}")


'''
https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers

'''
