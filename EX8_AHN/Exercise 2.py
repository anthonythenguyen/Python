def main():
    windChill = []
    for V in range(5, 50, 5):
        x = []
        for T in range(-20, 60, 10):
            temp = 35.74 + .6215 * T - 36.75*(V**.16) + .4275*T*(V**.16)
            x += [round(temp, 2)]
        windChill += [x]
    print('\n'.join([' '.join(['{:5}'.format(item) for item in row]) 
      for row in windChill]))
    
main()
