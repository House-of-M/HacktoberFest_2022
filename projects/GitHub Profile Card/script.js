const main = document.getElementById('main')
const form = document.getElementById('form')
const search = document.getElementById('search')
const gh_url = 'https://api.github.com/users/'

async function getUser(username) {
    try {
        const { data } = await axios(gh_url + username)
        createUserCard(data)
        getRepos(username)
    } catch(err) {
        if(err.response.status == 404) {
            createErrorCard('No profile found')}
    }
}

async function getRepos(username) {
    try {
        const { data } = await axios(gh_url + username + '/repos?sort=created')
        addReposToCard(data)
    } catch(err) {
        createErrorCard('Cant feth repos')
    }
}

function createUserCard(user) {
    const profileID = user.name || user.login || user.href
    const profileBio = user.bio ? `<p>${user.bio}</p>` : ''
    const cardHTML = `
    <div class="card">
    <div>
    <a href="${user.html_url}" target="_blank">
      <img src="${user.avatar_url}" alt="${user.name}" class="avatar">
    </a>
    </div>
    <div class="user-info">
    <a href="${user.html_url}" target="_blank">
      <h2>${profileID}</h2>
    </a>
      ${profileBio}
      <ul>
        <li><a href="${user.html_url}?tab=followers" target="_blank">${user.followers} <strong>Followers</strong></a></li>
        <li><a href="${user.html_url}?tab=following" target="_blank">${user.following} <strong>Following</strong></a></li>
        <li><a href="${user.html_url}?tab=repositories" target="_blank">${user.public_repos} <strong>Repos</strong></a></li>
        <li><a href="${user.html_url}?tab=achievements" target="_blank"><strong>Achievements</strong></a></li>
      </ul>
      <div id="repos"></div>
    </div>
  </div>
    `
    main.innerHTML = cardHTML
    
}

function createErrorCard(msg) {
    const cardHTML = `
        <div class="card">
            <h1>${msg}</h1>
        </div>
    `

    main.innerHTML = cardHTML
}

function addReposToCard(repos) {
    const reposEl = document.getElementById('repos')

    repos
        .slice(0,6)
        .forEach(repo => {
            const repoEl = document.createElement('a')
            repoEl.classList.add('repo')
            repoEl.href = repo.html_url
            repoEl.target = '_blank'
            repoEl.innerText = repo.name

            reposEl.appendChild(repoEl)
        })
}

form.addEventListener('submit', (e) => {
    e.preventDefault()

    const user = search.value

    if(user) {
        getUser(user)

        search.value = ''
    }
})