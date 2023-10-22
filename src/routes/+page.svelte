<script>
	const GRAFANA_URL = 'http://localhost:26658/public-dashboards/b9242c12e1354ec2992018c3085e3544'

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
	<iframe title="All Balances" src={GRAFANA_URL} width="1150" height="1700" frameborder="0" />
</div>

<style>
	.container {
		margin-top: 10px;
		margin-left: 80px;
	}
</style>
