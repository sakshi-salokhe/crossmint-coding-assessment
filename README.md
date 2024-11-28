# crossmint-coding-assessment

# Getting Started

Install requirements mentioned in the requirements.txt file.
To install all requirements at once, run this command: `pip3 install requirements.txt`

# Running the code

- Open terminal and go to the directory of these codes.
- Create a copy of the `.env.example` file and rename it `.env`.
  Paste correct values in the `.env` file for each variable.

- To create megaverse, run the following command:
  `python3 main.py create`

- To delete an accidentally created object:
  `python3 main.py <object_url_suffix> <row_value> <column_value>` <br/>
  where, `object_url_suffix` can be `polyanets`, `soloons` or `comeths`
  `row_value` and `column_value` together mention the position of the object