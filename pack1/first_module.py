print('this is always be run')


def main():
    print('first module main methos,name :{}',format(__name__))



if __name__=='__main__':
    main()

    print('running directly')
else:
    print('running from import')