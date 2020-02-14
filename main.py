from reader import reader

if __name__ == "__main__":
    R,C,F,N,B,T,rides = reader("a_example.in")
    print(R)
    for ride in rides:
        print(rides[ride])
