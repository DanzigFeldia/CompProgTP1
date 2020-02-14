from reader import reader

if __name__ == "__main__":
    R,C,F,N,B,T,rides = reader("a_example.in")
    for ride in rides:
        print(rides[ride])
