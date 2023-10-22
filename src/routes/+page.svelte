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
	let url = '';
	$: inputUrl = url;
</script>

<input type="text" placeholder="Enter your grafana url" bind:value={url} />
<div class="container">
	<iframe
		title="All Balances"
		src={inputUrl || GRAFANA_URL}
		width="1650"
		height="1700"
		frameborder="0"
	/>
</div>

<style>
	.container {
		margin-top: 10px;
		margin-left: 80px;
	}

	input {
		border-radius: 5px;
		padding: 3px;
		width: 250px;
		background: rgb(17, 17, 20);
		color: white;
		margin-top: 5px;
		margin-left: 5px;
	}
</style>
