<script>
	import ChainsSelect from '$lib/components/ChainsSelect.svelte';
	import { postClaim } from '$lib/actions/postClaim';

	/**
	 * @type {any}
	 */
	let selectedChain;

	function handleClaim() {
		postClaim(selectedChain.ledger_id, 'public_address'); // todo: update address
	}
</script>

<div class="sidebar">
	<div class="flex pt-4 header">
		<img class="logo" src="/logo4.png" alt="logo" />
		<div class="title">
			<div>HYDRATION</div>
			<div>STATION</div>
		</div>
	</div>
	<div class="content">
		<div class="pt-20">
			<div>
				<ChainsSelect selected={selectedChain} />
			</div>
		</div>

		<div>
			<div class="px-2 mb-4">
				<button on:click={handleClaim} type="button" class="btn variant-ghost-secondary w-full"
					>Claim</button
				>
			</div>
			<img class="faucet-img" src="/faucet2.png" alt="faucet" />
		</div>
	</div>
</div>

<style>
	.title {
		font-weight: 700;
		letter-spacing: 1.6px;
		font-size: 20px;
		line-height: 20px;
		color: #b2eafd;
	}

	.faucet-img {
		width: 200px;
		height: auto;
	}

	.sidebar {
		background: rgb(0, 0, 0);
		background: linear-gradient(
			180deg,
			rgba(0, 0, 0, 1) 25%,
			rgba(21, 34, 69, 0.7567620798319328) 43%,
			rgba(0, 0, 0, 1) 69%
		);

		color: aliceblue;
		height: 100%;
		border-right: 1px solid rgb(11, 11, 52);
	}

	.content {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		padding: 0 15px 10px;
		height: 88vh;
	}

	.logo {
		width: 40px;
		height: 35px;
		margin: 0 7px;
	}
</style>
