<template>
    <div id="app" ref="testHtml">
        <h1>Test heading </h1>
        <div class="card">
            <div class="card-header">
                Featured
            </div>
            <div class="card-body">
                <h5 class="card-title">Special title treatment</h5>
                <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>
        <div class="card">
            <div class="card-header">
                Featured
            </div>
            <div class="card-body">
                <h5 class="card-title">Special title treatment</h5>
                <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>
        <button class="btn btn-danger" @click="generatePdf">generate PDF</button>
    </div>


</template>

<script>
new Vue({
    el: '#app',
    data() {
        return {
            message: 'Hi my first vue code pen!!!'
        }
    },
    methods: {
        //jspdf does not include the bootstrap style layout
        generatePdf() {
            var doc = new jsPDF('p', 'pt', 'A4');
            margins = {
                top: 80,
                bottom: 60,
                left: 40,
                width: 522
            };

            doc.fromHTML(this.$refs.testHtml, margins.left, margins.top, {
                'width': margins.width
            });

            doc.save('test.pdf');
        }
    }
})
</script>

<style>

</style>