def fun(i=1):

    if(i <= 5):
        print(i)
        i = i + 1

        fun(i)  # Reccursive call


def main():

    fun();


if __name__ == '__main__':
        main()    