const body = document.querySelector('body');
const tbody = document.querySelector('tbody')
const btnAddUpdate = document.querySelector('#btnAddUpdate')
const inNickname = document.querySelector('#inNickname')
const inEmail = document.querySelector('#inEmail')
const inPassword = document.querySelector('#inPassword')

btnAddUpdate.onclick = btnAddUser

body.onload = () => {
    fillTable()
}

function createRow(u, i){
    const tr = document.createElement('tr')
    //Delete
    const tdDelete = document.createElement('td')
    const iDelete = document.createElement('i')
    iDelete.className = 'fas fa-trash'
    iDelete.onclick = () => {
        const isConfirm = confirm('¿Seguro?')
        if(isConfirm){
            deleteUser(i)
            clearTable()
            fillTable()
        }
    }
    //Update
    const tdUpdate = document.createElement('td')
    const iUpdate = document.createElement('i')
    iUpdate.className = 'fas fa-pen'
    iUpdate.onclick = () => {
        btnAddUpdate.textContent = 'ACTUALIZAR'
        inNickname.value = u.nickname
        inPassword.value = u.password
        inEmail.value = u.email
        btnAddUpdate.onclick = (e) => btnUpdateUser(e, i)
    }
    //Nickname
    const tdNickname = document.createElement('td')
    tdNickname.textContent = u.nickname
    //Email
    const tdEmail = document.createElement('td')
    tdEmail.textContent = u.email
    //Password
    const tdPassword = document.createElement('td')
    tdPassword.textContent = u.password
    //JOIN
    tdDelete.appendChild(iDelete)
    tdUpdate.appendChild(iUpdate)
    tr.append(tdDelete, tdUpdate,tdNickname, tdEmail, tdPassword)

    return tr;
}


function btnAddUser(e){
    const i = getUsers().length
    const newUser = createUser(inNickname.value, inEmail.value, inPassword.value)
    const tr = createRow(newUser, i)
    tbody.appendChild(tr)
    e.preventDefault()
    alert("Elemento guardado")
}

function btnUpdateUser(e, i){
    updateUser(i, inNickname.value, inEmail.value, inPassword.value)
    clearTable()
    fillTable()
    e.preventDefault()
    alert("Elemento actualizado")
    inNickname.value = ''
    inEmail.value = ''
    inPassword.value = ''
    btnAddUpdate.textContent = 'Agregar'
    btnAddUpdate.onclick = btnAddUser
}

function clearTable(){
    tbody.innerHTML = ''
}

function  fillTable(){
    let trs = [];
    const users = getUsers(); 
    users.forEach((u, i)=>{
        const tr = createRow(u, i)
        trs.push(tr)  
    })
    //join with tbody
    tbody.append(...trs)
}