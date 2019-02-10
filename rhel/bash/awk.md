### AWK

- awk utility is powerful data manipulation/scripting programming language (In fact based on the C programming Language). 

- Use awk to handle complex task such as calculation, database handling, report creation etc.

#### General Syntax of awk:
- `awk -f {awk program file} filename`
- awk reads the input from given file (or from stdin also) one line at a time, then each line is compared with pattern. 
- If pattern is match for each line then given action is taken. Pattern can be regular expressions. Following is the summery of common awk metacharacters:
- . (Dot)	Match any character
- \*	Match zero or more character
- ^	Match beginning of line
- $	Match end of line
- \	Escape character following
- \[ ]	List
- { }	Match range of instance
- \+	Match one more preceding
- ?	Match zero or one preceding
- |	Separate choices to match

##### NR and NF are predefined variables of awk which means Number of input Record, Number of Fields in input record respectively. 

|awk Variable   |Meaning   |   
|---|---|---|
|FILENAME   |Name of current input file   |   
|RS   |Input record separator character (Default is new line)   |   
|OFS   |Output field separator string (Blank is default)   |   
|ORS   |Output record separator string (Default is new line) |
|NF   |Number of input record|  
|NR   |Number of fields in input record|  
|OFMT   |Output format of number|
|FS   |Field separator character (Blank & tab is default)|  
								