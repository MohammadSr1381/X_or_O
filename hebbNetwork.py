import numpy as np
import pandas
import ast



class HebbNetwork :
    
    
    def __init__(self):
        
        self.weights = np.zeros((5,5))
        self.bias = 0
        self.weight_calculation()
    

    
    def dataset(self):
        
        data_frame = pandas.read_csv("dataset.csv")
        
        data_frame_labels = data_frame["label"]
        data_frame_data = data_frame["data"].apply(ast.literal_eval)
        
        output_arrays = np.array(data_frame_labels)
        input_arrays = np.array(data_frame_data)
        return output_arrays , input_arrays

    
    
    def weight_calculation(self):
        
        patterns = self.dataset() 
        y , x = patterns
        
        for i in range(len(y)):
            self.bias += y[i]
            for j in range(len(x[i])): 
                for k in range(len(x[i][j])):
                    delta_weights = 0
                    delta_weights = x[i][j][k] * y[i]
                    self.weights[j][k] = self.weights[j][k] + delta_weights      
          
        
        
    def classify(self , data):
        print(self.weights)
        output = 0
        test_data = data
        for i in range(len(test_data)):
            for j in range(len(test_data)):
                output += data[i][j] * self.weights[i][j]
                
        output += self.bias
        
        if output >= 0 :
            return True
        else : return False


"""      
1,"[[1, -1, 1, -1, -1], [-1, 1, -1, -1, -1], [1, -1, 1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]"
-1,"[[1, 1, 1, 1, 1], [1, -1, -1, -1, 1], [1, -1, -1, -1, 1], [1, -1, -1, -1, 1], [1, 1, 1, 1, 1]]"
1,"[[1, -1, -1, 1, -1], [-1, 1, 1, -1, -1], [-1, 1, 1, -1, -1], [1, -1, -1, 1, -1], [-1, -1, -1, -1, -1]]"
1,"[[-1, -1, -1, -1, -1], [-1, 1, -1, 1, -1], [-1, -1, 1, -1, -1], [-1, 1, -1, 1, -1], [-1, -1, -1, -1, -1]]"
-1,"[[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, 1, 1, 1, -1], [-1, 1, -1, 1, -1], [-1, 1, 1, 1, -1]]"
-1,"[[-1, 1, 1, 1, 1], [-1, 1, 1, -1, 1], [-1, 1, -1, -1, 1], [-1, 1, -1, -1, 1], [-1, 1, 1, 1, 1]]"

"""
        
