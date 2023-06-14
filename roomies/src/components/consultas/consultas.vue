<template>
    <div class="card-header card-header-divider text-center fs-4">   Listado de Consultas
        <p class="lead">Consultas preDefinidas que te permitiran observar como se conforma un poco Roomies.</p>
        <br />
    </div>
    <ul class="nav nav-tabs" role="tablist">
        <li class="nav-item" role="presentation">
          <a class="nav-link" data-bs-toggle="tab" href="#consulta1" aria-selected="true" tabindex="-1" role="tab">Consulta Numero 1</a>
        </li>
        <li class="nav-item" role="presentation">
          <a class="nav-link" data-bs-toggle="tab" href="#consulta2" aria-selected="true" tabindex="-1" role="tab">Consulta Numero 2</a>
        </li>
        <li class="nav-item" role="presentation">
          <a class="nav-link" data-bs-toggle="tab" href="#consulta3" aria-selected="true" tabindex="-1" role="tab">Consulta Numero 3</a>
        </li>
        <li class="nav-item" role="presentation">
          <a class="nav-link" data-bs-toggle="tab" href="#consulta4" aria-selected="true" tabindex="-1" role="tab">Consulta Numero 4</a>
        </li>
        <li class="nav-item" role="presentation">
          <a class="nav-link" data-bs-toggle="tab" href="#consulta5" aria-selected="true" tabindex="-1" role="tab">Consulta Numero 5</a>
        </li>
        <li class="nav-item" role="presentation">
          <a class="nav-link" data-bs-toggle="tab" href="#consulta6" aria-selected="true" tabindex="-1" role="tab">Consulta Numero 6</a>
        </li>
      </ul>
      <div id="myTabContent" class="tab-content">
        <div class="tab-pane fade show active" id="consulta1" role="tabpanel">
            <div class="alert alert-dismissible alert-info">
                <center>
                    <p>Mostrar todos los Clientes y la cantidad de hombres, como la de mujeres que hacen parte de Roomies.</p>
                    <a href="/consulta1" class="boton">Ir a la Consulta</a>
                </center>
            </div>
        </div>
        <div class="tab-pane fade show active" id="consulta2" role="tabpanel">
            <div class="alert alert-dismissible alert-info">
                <center>
                    <p>Mostrar Pagos por fecha de los Clientes que hacen parte de Roomies.</p>
                    <a href="/consulta2" class="boton">Ir a la Consulta</a>
                </center>
            </div>
        </div>
        <div class="tab-pane fade show active" id="consulta3" role="tabpanel">
            <div class="alert alert-dismissible alert-info">
                <center>
                    <p>Mostrar Fecha de inicio precio y fecha final de los alquileres disponibles.</p>
                    <a href="/consulta3" class="boton">Ir a la Consulta</a>
                </center>
            </div>
        </div>
        <div class="tab-pane fade show active" id="consulta4" role="tabpanel">
            <div class="alert alert-dismissible alert-info">
                <center>
                    <p>Consulta con utilizacion de SQL para, para realizar la sigiente busquedad.
                        &nbsp; "SELECT id, nombre, ciudad, correo FROM tbl_persona;"...</p>
                    <a href="/consulta4" class="boton">Ir a la Consulta</a>
                </center>
            </div>
        </div>
        <div class="tab-pane fade show active" id="consulta5" role="tabpanel">
            <div class="alert alert-dismissible alert-info">
                <center>
                    <p>Consulta a la tabla personas que nos retorna los registros, excluyendo a todo aquellos que contengan en el campo ciudad "San Juan"</p>
                    <a href="/consulta5" class="boton">Ir a la Consulta</a>
                </center>
            </div>
        </div>
        <div class="tab-pane fade show active" id="consulta5" role="tabpanel">
            <div class="alert alert-dismissible alert-info">
                <center>
                    <p>Consulta a la tabla personas que nos retorna los registros de forma ordenada...</p>
                    <a href="/consulta6" class="boton">Ir a la Consulta</a>
                </center>
            </div>
        </div>
      </div>
</template>

<script  lang="ts">
export default {}
</script>

<style scoped lang="css">

.boton {
	background-color:#637aad;
	border-radius:28px;
	border:1px solid #314179;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:19px;
	padding:6px 58px;
	text-decoration:none;
	text-shadow:0px 1px 0px #7a8eb9;
}
.boton:hover {
	background-color:#5972a7;
}
.boton:active {
	position:relative;
	top:1px;
}
</style>