import sys

def helloworld(out):
    """
    Printing a hello world message.

    Args:
        out: Output stream to write the message to.
    """
    out.write("Hello world of Python\n")

# Call the function with a file object
helloworld(sys.stdout)
