## In reality, we only have Ac data, which is the amount in plasma versus time relationship

I will test step by step

### (1) we still have Aa data, yet the loss function is changed into ||Ac - Ac_pred||, instead of the previous ||A - A_pred||

[Code](https://github.com/yingzibu/ODE/blob/main/experiment/PO/one_compartment/use_Aa_loss_Ac_only.ipynb)

![](train_Ac_only.gif)

![](M_estimate_loss_Ac_only.gif)
