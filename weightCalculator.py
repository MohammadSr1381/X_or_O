import numpy as np
import pandas
import ast


class WeightCalculator :
        
    def dataset(self):
        
        data_frame = pandas.read_csv("dataset.csv")
        
        data_frame_labels = data_frame["label"]
        data_frame_data = data_frame["data"].apply(ast.literal_eval)
        
        output_arrays = np.array(data_frame_labels)
        input_arrays = np.array(data_frame_data)
        print(input_arrays)
        return output_arrays , input_arrays
    
    
    
    def weight_calculation(self):

        patterns = self.dataset()
        weights = np.zeros((5,5))
        delta_weights = np.zeros((5,5))
        bias = 0
        y , x = patterns
        
        for i in range(len(y)):
            bias += y[i]
            for j in range(len(x[i])): 
                for k in range(len(x[i][j])):
        
                    delta_weights = x[i][j][k] * y[i]
                    weights[j][k] += delta_weights
                    print(delta_weights)
                    print(weights)

"""      
1,"[[1, -1, 1, -1, -1], [-1, 1, -1, -1, -1], [1, -1, 1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]"
-1,"[[1, 1, 1, 1, 1], [1, -1, -1, -1, 1], [1, -1, -1, -1, 1], [1, -1, -1, -1, 1], [1, 1, 1, 1, 1]]"
1,"[[1, -1, -1, 1, -1], [-1, 1, 1, -1, -1], [-1, 1, 1, -1, -1], [1, -1, -1, 1, -1], [-1, -1, -1, -1, -1]]"
1,"[[-1, -1, -1, -1, -1], [-1, 1, -1, 1, -1], [-1, -1, 1, -1, -1], [-1, 1, -1, 1, -1], [-1, -1, -1, -1, -1]]"
-1,"[[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, 1, 1, 1, -1], [-1, 1, -1, 1, -1], [-1, 1, 1, 1, -1]]"
-1,"[[-1, 1, 1, 1, 1], [-1, 1, 1, -1, 1], [-1, 1, -1, -1, 1], [-1, 1, -1, -1, 1], [-1, 1, 1, 1, 1]]"

"""
        
