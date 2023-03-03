# SWD-TEST


# SWD-TEST

Name : Thanathip Chansri

## Section 1
- 1.1 : https://github.com/sSlotty/SWD-TEST/blob/main/SWD_BACKEND_TEST-main/logical_test.py
- 1.2 : https://github.com/sSlotty/SWD-TEST/blob/main/SWD_BACKEND_TEST-main/logical_test_2.py
- 1.3 https://github.com/sSlotty/SWD-TEST/blob/main/SWD_BACKEND_TEST-main/apis/views/schools.py

## Sction 2
- 2.1 : https://github.com/sSlotty/SWD-TEST/tree/main/todos
- 2.2 : https://github.com/sSlotty/SWD-TEST/tree/main/mail
- 2.3 : https://github.com/sSlotty/SWD-TEST/blob/main/SWD_BACKEND_TEST-main/index_max_values.py
- 2.4 : https://github.com/sSlotty/SWD-TEST/blob/main/SWD_BACKEND_TEST-main/zero_last_digit_fac.py



## API Reference School 

#### Create student score

```http
  POST /api/student_score/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `first_name` | `string` | **Required**. first name |
| `last_name` | `string` | **Required**. last name |
| `subject_title` | `string` | **Required**. subject title |
| `score` | `integer` | **Required**.  score |


#### Get student score

```http
  GET /api/student_score/${student_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `student_id`      | `string` | **Required**. id of student |

#### Get personnel detail 

```http
  GET /api/personnel_details/${school_name}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `school_name`      | `string` | **Required**. name of school |

#### Get School heirarchy 

```http
  GET /api/school_hierarchy/
```

#### Get school structure 

```http
  GET /api/school_structure/
```


## API Reference TODO 

#### Create todo

```http
  POST /api/todo/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | **Required**. first name |
| `description` | `string` | **Required**. last name |



#### Get all todo

```http
  GET /api/todo/
```

#### Get todo by tiele 

```http
  GET /api/todo/${title}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. title of todo |

#### Delete Todo by title 

```http
  DELETE /api/todo/${title}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. title of todo |

#### Update Todo by title 

```http
  PUT /api/todo/${title}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title` | `string` | **Required**. first name |
| `description` | `string` | **Required**. last name |


## API Reference Send-Email 

#### Send mail

```http
  POST /api/send/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `subject` | `string` | **Required**. subject |
| `message` | `string` | **Required**. message |
| `name` | `string` | **Required**. name of recipient |
| `to` | `string` | **Required**. email of recipient |





