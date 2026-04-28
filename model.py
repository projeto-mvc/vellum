from dao import connection

def consulta_alunos():
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(''' SELECT * FROM alunos''')
    dados = cursor.fetchall()
    conn.close()
    return dados

def consultar_id(id):
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(''' SELECT * FROM alunos WHERE id = %s''', (id,))
    dados = cursor.fetchone()
    conn.close()
    return dados

def add_aluno(nome, email, curso_id):
    conn = connection()
    cursor = conn.cursor()
    
    query = '''
            insert into alunos (nome, email, curso_id) 
            values (%s, %s, %s)
            '''
            
    cursor.execute(query , (nome, email, curso_id))

    conn.commit()
    conn.close()

def update_aluno(id, nome, email, curso_id):
    conn = connection()
    cursor = conn.cursor()
    
    query = '''
            UPDATE alunos
            SET nome = %s,
                email = %s,
                curso_id = %s
            WHERE id = %s

            '''

    cursor.execute(query, (nome, email, curso_id, id))
    conn.commit()
    conn.close()

