import pandas as pd 
import bambi as bmb
import arviz as az

national_working_long=pd.read_csv("national_working_long.csv")


# model specification:
model_variables = ['response','rurality','race_selfid_original', 'sample', 'age', 'sex', 'education', 'income', 'homeownership', 'numchild', 'disability', 'coping_appraisal', 'threat_appraisal','dis_iexp']
national_working_long = national_working_long.dropna(subset=model_variables)
print(national_working_long[national_working_long['sample'] == 'National'])

#data manipulation

national_working_long['rurality'] = national_working_long['rurality'].astype('category')
national_working_long['item'] = national_working_long['item'].astype('category')
national_working_long['sample'] = national_working_long['sample'].astype('category')
national_working_long['id'] = national_working_long['id'].astype('category')
national_working_long = national_working_long[national_working_long['race_selfid_original'] != "Other (please specify):"]

national_working_long['race_selfid_original'] = national_working_long['race_selfid_original'].astype('category')



#model work_flow
categories = national_working_long['sample'].cat.categories.tolist()
if 'National' in categories:
    new_order = ['National'] + [cat for cat in categories if cat != 'National']
    national_working_long['sample'] = national_working_long['sample'].cat.reorder_categories(
        new_order, ordered=True
    )
else:
    print("'National' not found in categories!")


formula = 'response ~ sample * (age + sex + education +dis_iexp + income + homeownership + numchild + disability + coping_appraisal + threat_appraisal) + (1|id) + (1|item)'
priors = {
    "Intercept": bmb.Prior("Normal", mu=0, sigma=0.5),
    "b": bmb.Prior("Normal", mu=0, sigma=0.5),
    "sd": bmb.Prior("Normal", mu=0, sigma=0.5),
}

model_fancy2 = bmb.Model(formula, national_working_long, family="bernoulli", priors=priors)
fitted_model2 = model_fancy2.fit(
    draws=2000,
    chains=16,
    cores=16,
    tune=2000,
    target_accept=0.95,
    max_treedepth=15
)

print(az.summary(fitted_model2))
az.to_netcdf(fitted_model2, "final_qiuqiule.nc")

