## Environment

```shell
sqlalchemy==1.4.19
pyqt5==5.15.4
```

## Usage

1. Create Database

   - use your `Mysql`  to create a database named 'bank_system'

2. Set config

   - go to [config](configs/db_config.py), and change your db information

3. Create database

   - go to [db.py](db.py), and change `debug=1`

   - run `db.py`

     ```python
     python db.py
     ```

   - remember set back debug = 0

4. Go and use it!

   ```python
   python main.py
   ```

   

