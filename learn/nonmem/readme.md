## Further modification needed:


1. NLLLoss could be normalized based on patient, instead of entries (multiple time points)

2. Currently 90% Confidence interval is calculated based on 1000 simulations. How do the popPK do CI calculation and how to reject/accept BE?


#### Current calculation is done by

1. Calculate pop parameters, once optimied, it could be fixed / trainable
2. initiate the $\eta \sim \mathcal{N}(0, \omega)$, and each patient's param has its unique $\eta$
    i.e. for dataset with patient num $= n$, random initiation $$\mathbf{\eta} \sim \mathcal{N}(0, \mathbf{\omega}),  \mathbf{\eta}\in \mathbb{R}^n, $$
3. then train the model to minimize NLLLoss, once trained the whole dataset, update $\mathbf{\omega} = \text{var} (\mathbf{\eta})$,
   train multiple epochs until the loss does not drop, stop train.
  * Problem 1: mean of $\mathbf{\eta}$ may not be $\mathbf{0}$.
  * Problem 2: is this method the same as the NONMEM?  
4.  Best model with the lowest loss is saved and reload to obtain the calculated $\mathbf{omega}$
5.  90% CI was calculated based on 1000 simulations on $\eta \sim \mathcal{N}(0, \omega)$


 | gradient descent |  fixed pop params   | trainable pop params 
:-----:|:-------------------------:|:-------------------------:
|overall comparison| ![](fig/nn_no_train_pop.png)  | ![](fig/nn_train_pop.png) 
| prediction | ![](fig/nn_no_train_pop_pred.png) | ![](fig/nn_train_pop_pred.png) 


