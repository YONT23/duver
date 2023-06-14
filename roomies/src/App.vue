<template>
  <Layout>
    <Header>
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Trabajo Final</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor01"
            aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarColor01">
            <ul class="navbar-nav me-auto">
              <li class="nav-item active">
                <a class="nav-link" href="/home">Inicio
                  <span class="visually-hidden">(Mendoza)</span>
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/servicios">Servicios</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/clientes">Personas</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/consultas">Consultas</a>
              </li>
            </ul>
            <form class="d-flex">
              <input class="form-control me-sm-2" type="text" placeholder="Search">
              <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
            </form>
          </div>
        </div>
      </nav>
      <br>
    </Header>
    <Layout>
      <Content>
        <router-view />
      </Content>
    </Layout>
  </Layout>
</template>

<script lang="ts">
export default {}
</script>

<style>
</style>