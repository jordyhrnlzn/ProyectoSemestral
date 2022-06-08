const users = [
    new User('DeadByDaylight', 'Terror','2016'),
    new User('Minecraft', 'Aventura','2009'),
    new User('Fortnite', 'shooter','2016'),
    new User('Terraria', 'Aventura','2012'),
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

