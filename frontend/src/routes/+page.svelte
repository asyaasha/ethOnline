<script>
  import { env } from '$env/dynamic/public';

  const GRAFANA_URL = `http://${env.PUBLIC_GRAFANA_URL}` || '';

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
  $: faucetAdddress = '0x5206Cb0140B3a3C12833e12235d1654Ceec02C94';
  const txns = [];
</script>


<div>
	<input type="text" placeholder="Enter your grafana url" bind:value={url} />
	<div class="connected mt-2 ml-2">
		Connected to: {inputUrl || GRAFANA_URL}
	</div>
	<div class="connected mt-2 ml-2">
		Faucet Address: {faucetAdddress}
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
