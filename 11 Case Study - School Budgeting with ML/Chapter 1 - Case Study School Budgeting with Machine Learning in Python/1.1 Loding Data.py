'''
Loading the data
Now it's time to check out the dataset! You'll use pandas (which has been pre-imported as pd) to load your data into a DataFrame and then do some Exploratory Data Analysis (EDA) of it.

The training data is available as TrainingData.csv. Your first task is to load it into a DataFrame in the IPython Shell using pd.read_csv() along with the keyword argument index_col=0.

Use methods such as .info(), .head(), and .tail() to explore the budget data and the properties of the features and labels.

Some of the column names correspond to features - descriptions of the budget items - such as the Job_Title_Description column. The values in this column tell us if a budget item is for a teacher, custodian, or other employee.

Some columns correspond to the budget item labels you will be trying to predict with your model. For example, the Object_Type column describes whether the budget item is related classroom supplies, salary, travel expenses, etc.

Use df.info() in the IPython Shell to answer the following questions:

How many rows are there in the training data?
How many columns are there in the training data?
How many non-null entries are in the Job_Title_Description column?
Instructions
50 XP
Instructions
50 XP
Possible Answers

25 rows, 1560 columns, 1560 non-null entries in Job_Title_Description.

25 rows, 1560 columns, 1131 non-null entries in Job_Title_Description.

1560 rows, 25 columns, 1131 non-null entries in Job_Title_Description.

1560 rows, 25 columns, 1560 non-null entries in Job_Title_Description.
'''

df=pd.read_csv("TrainingData.csv")
In [3]:
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1560 entries, 0 to 1559
Data columns (total 26 columns):
Unnamed: 0                1560 non-null int64
Function                  1560 non-null object
Use                       1560 non-null object
Sharing                   1560 non-null object
Reporting                 1560 non-null object
Student_Type              1560 non-null object
Position_Type             1560 non-null object
Object_Type               1560 non-null object
Pre_K                     1560 non-null object
Operating_Status          1560 non-null object
Object_Description        1461 non-null object
Text_2                    382 non-null object
SubFund_Description       1183 non-null object
Job_Title_Description     1131 non-null object
Text_3                    296 non-null object
Text_4                    193 non-null object
Sub_Object_Description    364 non-null object
Location_Description      874 non-null object
FTE                       449 non-null float64
Function_Description      1340 non-null object
Facility_or_Department    252 non-null object
Position_Extra            1026 non-null object
Total                     1542 non-null float64
Program_Description       1192 non-null object
Fund_Description          819 non-null object
Text_1                    1132 non-null object
dtypes: float64(2), int64(1), object(23)
memory usage: 317.0+ KB
In [4]:
df.describe()
Out[4]:

          Unnamed: 0         FTE         Total
count    1560.000000  449.000000  1.542000e+03
mean   227767.180128    0.493532  1.446867e+04
std    130207.535688    0.452844  7.916752e+04
min       198.000000   -0.002369 -1.044084e+06
25%    113690.750000    0.004310  1.108111e+02
50%    226445.500000    0.440000  7.060299e+02
75%    340883.500000    1.000000  5.347760e+03
max    450277.000000    1.047222  1.367500e+06
In [5]:
df.head()
Out[5]:

   Unnamed: 0                Function          Use          Sharing   Reporting Student_Type Position_Type               Object_Type     Pre_K  ... Location_Description  FTE                  Function_Description      Facility_or_Department Position_Extra     Total                                Program_Description                                   Fund_Description                Text_1
0         198                NO_LABEL     NO_LABEL         NO_LABEL    NO_LABEL     NO_LABEL      NO_LABEL                  NO_LABEL  NO_LABEL  ...                  NaN  NaN  Care and Upkeep of Building Services                         NaN            NaN  -8291.86                                                NaN  Title I - Disadvantaged Children/Targeted Assi...    TITLE I CARRYOVER 
1         209  Student Transportation     NO_LABEL  Shared Services  Non-School     NO_LABEL      NO_LABEL    Other Non-Compensation  NO_LABEL  ...      ADMIN. SERVICES  NaN             STUDENT TRANSPORT SERVICE                         NaN            NaN    618.29                               PUPIL TRANSPORTATION                                       General Fund                   NaN
2         750    Teacher Compensation  Instruction  School Reported      School  Unspecified       Teacher  Base Salary/Compensation  Non PreK  ...                  NaN  1.0                                   NaN                         NaN        TEACHER  49768.82                              Instruction - Regular                             General Purpose School                   NaN
3         931                NO_LABEL     NO_LABEL         NO_LABEL    NO_LABEL     NO_LABEL      NO_LABEL                  NO_LABEL  NO_LABEL  ...                  NaN  NaN                           Instruction  Instruction And Curriculum            NaN     -1.02  "Title I, Part A Schoolwide Activities Related...                             General Operating Fund                   NaN
4        1524                NO_LABEL     NO_LABEL         NO_LABEL    NO_LABEL     NO_LABEL      NO_LABEL                  NO_LABEL  NO_LABEL  ...                  NaN  NaN            Other Community Services *                         NaN            NaN   2304.43                                                NaN  Title I - Disadvantaged Children/Targeted Assi...   TITLE I PI+HOMELESS

[5 rows x 26 columns]