const users = [
    new User('BRYAN', 'ypz@gmail.com','Bryansarmineto02.'),
    new User('CATALINA', 'gn2@gmail.com','CATA2p.'),
    new User('JAVIER', 'abril@gmail.com','GONZalez155.'),
    new User('JORDY', 'febrery@gmail.com','ALJordy2003.'),
]

function getUsers(){
    return users
}

function createUser(nickname, email, password){
    const newUser = new User(nickname, email, password)
    users.push(newUser)
    return newUser
}

function updateUser(i, newNickname, newEmail, newPassword){
    users[i].nickname = newNickname
    users[i].email = newEmail
    users[i].password = newPassword
}

function deleteUser(i){
    users.splice(i, 1)
}

