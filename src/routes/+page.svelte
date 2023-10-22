<script>
	const GRAFANA_URL = 'http://localhost:26658/public-dashboards/04a1eea4e60d405c88594ca10aecdce5';

	$: bgImage = `
    background-image: url("/bg.png");
    background-size: cover;
    background-position: center;
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;`;
</script>

<div class="container">
	<iframe title="All Balances" src={GRAFANA_URL} width="850" height="700" frameborder="0" />
</div>

<style>
	.container {
		margin-top: 10px;
		margin-left: 80px;
	}
</style>
