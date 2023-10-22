<script>
	const GRAFANA_URL = ''

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


<div>
	<input type="text" placeholder="Enter your grafana url" bind:value={url} />
	<div class="connected mt-2 ml-2">
		Connected to: {inputUrl || GRAFANA_URL}
	</div>
</div>
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
		width: 350px;
		background: rgb(17, 17, 20);
		color: white;
		margin-top: 5px;
		margin-left: 5px;
		border: 0.8px solid #258dc9b7;
	}
	.connected {
		color: #258dc9b7;
	}
</style>
