import numpy as np

class NeuralNetwork():
    def __init__(self):
        # np.random.seed(1) ????
        self.weights = np.array([[0] * 63]*7) #Weights initialized to 0
        self.bias = np.array([0] * 7)      #Bias initialized to 0


    def hardlimit(self, x): #hardlimit function
        for i in range(len(x)):
            if x[i] > 0:
                x[i] = 1
            elif x[i] == 0:
                x[i] = 0
            else:
                x[i] = -1
        return x

    def update(self,w,e,p):                         #update weights
        ep = np.matmul(np.matrix.transpose(e), p)   #EP 
        w = w + ep                                  # W = W + EP updated weights
        return w


    def train(self, inputs, outputs, epoch):
        for iteration in range(epoch):
            # output = predict(inputs)
            print(iteration)
            print(type(inputs))

            n = np.matmul(self.weights, inputs.transpose())  #N = WP
            # print(len(self.bias))
            n = np.matrix.transpose(n) + self.bias          #N + B

            # print(len(self.bias))
            # for i in range(len(n)):
            #     n[i] += self.bias

            # print("N:")
            # print(n)
            # print("Bias:")
            # print(self.bias)
            a = []                                          #append values to a
            for value in n:
                a.append(self.hardlimit(value))

            a = np.array(a)
            # print("A:")
            # print(a)

            # print("Output:")
            # print(outputs)
            e = outputs - a
            print("error:" ,e)
            # print("E:")
            # print(e)

            print("Before update Weights: ",len(self.weights), len(self.weights[0]),"\n" ,self.weights)
            print(self.weights)

            # print("Inputs:")
            # print(inputs)

            self.weights= self.update(self.weights, e, inputs)
            print("After update Weights: ",len(self.weights), len(self.weights[0]),"\n" ,self.weights)

            for i in range(len(self.bias)):
                self.bias[i] += sum([j[i] for j in e])
            # self.bias = self.bias + e

    def predict(self, inputs):
        # inputs = inputs.astype(float)
        output = self.hardlimit(np.matmul(self.weights,inputs) + self.bias)
        return output

def inputstuff():
    # letters = [
    # np.matrix('0 0 1 1 0 0 0; 0 0 0 1 0 0 0; 0 0 0 1 0 0 0; 0 0 1 0 1 0 0; 0 0 1 0 1 0 0; 0 1 1 1 1 1 0; 0 1 0 0 0 1 0; 0 1 0 0 0 1 0; 1 1 1 0 1 1 1'),
    # np.matrix('0 0 0 1 0 0 0; 0 0 0 1 0 0 0; 0 0 0 1 0 0 0; 0 0 1 0 1 0 0; 0 0 1 0 1 0 0; 0 1 0 0 0 1 0; 0 1 1 1 1 1 0; 0 1 0 0 0 1 0; 0 1 0 0 0 1 0'),
    # np.matrix('0 0 0 1 0 0 0; 0 0 0 1 0 0 0; 0 0 1 0 1 0 0; 0 0 1 0 1 0 0; 0 1 0 0 0 1 0; 0 1 1 1 1 1 0; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 1 0 0 0 1 1'),
    # np.matrix('1 1 1 1 1 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 1 1 1 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 1 1 1 1 1 1 0'),
    # np.matrix('1 1 1 1 1 1 0; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 1 1 1 1 1 0; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 1 1 1 1 1 0'),
    # np.matrix('1 1 1 1 1 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 1 1 1 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 1 1 1 1 1 1 0'),
    # np.matrix('0 0 1 1 1 1 1; 0 1 0 0 0 0 1; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 0 1 0 0 0 0 1; 0 0 1 1 1 1 0'),
    # np.matrix('0 0 1 1 1 0 0; 0 1 0 0 0 1 0; 1 0 0 0 0 0 1; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 1; 0 1 0 0 0 1 0; 0 0 1 1 1 0 0'),
    # np.matrix('0 0 1 1 1 0 1; 0 1 0 0 0 1 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 1; 0 1 0 0 0 1 0; 0 0 1 1 1 0 0'),
    # np.matrix('1 1 1 1 1 0 0; 0 1 0 0 0 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 1 0 0; 1 1 1 1 1 0 0'),
    # np.matrix('1 1 1 1 1 0 0; 1 0 0 0 0 1 0; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 1 0; 1 1 1 1 1 0 0'),
    # np.matrix('1 1 1 1 1 0 0; 0 1 0 0 0 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 1 0 0; 1 1 1 1 1 0 0'),
    # np.matrix('1 1 1 1 1 1 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 0; 0 1 0 1 0 0 0; 0 1 1 1 0 0 0; 0 1 0 1 0 0 0; 0 1 0 0 0 0 0; 0 1 0 0 0 0 1; 1 1 1 1 1 1 1'),
    # np.matrix('1 1 1 1 1 1 1; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 1 1 1 1 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 1 1 1 1 1 1'),
    # np.matrix('1 1 1 1 1 1 1; 0 1 0 0 0 0 1; 0 1 0 0 1 0 0; 0 1 1 1 1 0 0; 0 1 0 0 1 0 0; 0 1 0 0 0 0 0; 0 1 0 0 0 0 0; 0 1 0 0 0 1 0; 1 1 1 1 1 1 1'),
    # np.matrix('0 0 0 1 1 1 1; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 1 0 0 0 1 0; 0 1 0 0 0 1 0; 0 0 1 1 1 0 0'),
    # np.matrix('0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 1 0 0 0 1 0; 0 1 0 0 0 1 0; 0 0 1 1 1 0 0'),
    # np.matrix('0 0 0 0 1 1 1; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 1 0 0 0 1 0; 0 0 1 1 1 0 0'),
    # np.matrix('1 1 1 0 0 1 1; 0 1 0 0 1 0 0; 0 1 0 1 0 0 0; 0 1 1 0 0 0 0; 0 1 1 0 0 0 0; 0 1 0 1 0 0 0; 0 1 0 0 1 0 0; 0 1 0 0 0 1 0; 1 1 1 0 0 1 1'),
    # np.matrix('1 0 0 0 0 1 0; 1 0 0 0 1 0 0; 1 0 0 1 0 0 0; 1 0 1 0 0 0 0; 1 1 0 0 0 0 0; 1 0 1 0 0 0 0; 1 0 0 1 0 0 0; 1 0 0 0 1 0 0; 1 0 0 0 0 1 0'),
    # np.matrix('1 1 1 0 0 1 1; 0 1 0 0 1 0 0; 0 1 0 1 0 0 0; 0 1 1 0 0 0 0; 0 1 1 0 0 0 0; 0 1 0 1 0 0 0; 0 1 0 0 1 0 0; 0 1 0 0 0 1 0; 1 1 1 0 0 1 1'),
    # ]

    # letters = np.array(letters).flatten


    #this is disgusting.....
    input = ["001100000010000001000001010000101000111110010001001000101110111", #A1
        "111111001000010100001010000101111100100001010000101000011111110",      #B1
        "001111101000011000000100000010000001000000100000001000010011110",      #C1
        "111110001000100100001010000101000010100001010000101000101111100",      #D1
        "111111101000010100000010100001110000101000010000001000011111111",      #E1
        "000111100000100000010000001000000100000010010001001000100011100",      #J1
        "111001101001000101000011000001100000101000010010001000101110011",      #K1
        "000100000010000001000001010000101000100010011111001000100100010",      #A2
        "111111010000011000001100000111111101000001100000110000011111110",      #B2
        "001110001000101000001100000010000001000000100000101000100011100",      #C2
        "111110010000101000001100000110000011000001100000110000101111100",      #D2
        "111111110000001000000100000011111001000000100000010000001111111",      #E2
        "000001000000100000010000001000000100000010010001001000100011100",      #J2
        "100001010001001001000101000011000001010000100100010001001000010",      #K2
        "000100000010000010100001010001000100111110100000110000011100011",      #A3
        "111111001000010100001011111001000010100001010000101000011111110",      #B3
        "001110101000111000001100000010000001000000100000101000100011100",      #C3
        "111110001000100100001010000101000010100001010000101000101111100",      #D3
        "111111101000010100100011110001001000100000010000001000011111111",      #E3
        "000011100000100000010000001000000100000010000001001000100011100",      #J3
        "111001101000100100100010100001100000101000010010001000101110011"]      #K3

    # for i in range(21):
    #     letters[i].flatten

    for i in range(len(input)):
        input[i] = [1 if int(j) else -1 for j in input[i]] # [21][63]
    input = np.array(input)

    return input
    # return letters

# def testdata():
#     letterc = np.array[]


def target():
    target = [[1,0,0,0,0,0,0],
		[0,1,0,0,0,0,0],
		[0,0,1,0,0,0,0],
		[0,0,0,1,0,0,0],
		[0,0,0,0,1,0,0],
		[0,0,0,0,0,1,0],
		[0,0,0,0,0,0,1]] * 3
    return np.array(target)

#flatten down the inputs and get the target vectors

# def main():
#     print("oops")


if __name__ == "__main__":
    # main()
    a = NeuralNetwork()
    # print(len(inputstuff()))
    print(inputstuff())
    a.train(inputstuff(), target(), 4)
    print("Predict:")
    for i in range(21):
      print(a.predict(inputstuff()[i]))
    print(a.weights)
    print(a.bias)

