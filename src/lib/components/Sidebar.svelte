<script>
	import { TabGroup, Tab } from '@skeletonlabs/skeleton';

	import { popup } from '@skeletonlabs/skeleton';
	import { enhance, applyAction } from '$app/forms';
	import { createWeb3Modal, defaultWagmiConfig } from '@web3modal/wagmi';
	import {
		mainnet,
		gnosis,
		sepolia,
		polygon,
		filecoin,
		filecoinCalibration,
		mantle,
		mantleTestnet,
		scrollSepolia,
		scrollTestnet
	} from '@wagmi/core/chains';
	import LedgerSelect from '$lib/components/LedgerSelect.svelte';
	import AddressSelect from '$lib/components/AddressSelect.svelte';
	import { getWeb3Details } from '$lib/utils';

	const chains = [
		mainnet,
		gnosis,
		sepolia,
		polygon,
		filecoin,
		filecoinCalibration,
		mantle,
		mantleTestnet,
		scrollSepolia,
		scrollTestnet
	];
	const projectId = '1b0aad06235a3007b00055160c73fe1d';
	const wagmiConfig = defaultWagmiConfig({
		chains,
		projectId
	});
	const modal = createWeb3Modal({ wagmiConfig, projectId, chains });

	/**
	 * @type {any}
	 */
	const popupHover = {
		event: 'hover',
		target: 'popupHover',
		placement: 'top'
	};

	/**
	 * @type {any}
	 */
	let selectedChain;
	let tabSet = 0;
	/**
	 * @type {any}
	 */
	let selectedAddress;

	let resMsg = '';
	let loading = false;

	/**
	 * @type {any}
	 */
	export let data;

	const { account } = getWeb3Details();
	$: if (resMsg) {
		setTimeout(() => {
			resMsg = '';
		}, 5000);
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
			<div class="pb-2">Claim from a faucet</div>
			<div>
				<LedgerSelect bind:selected={selectedChain} data={data?.ledgers || []} />
			</div>
		</div>

		<div>
			<div class="px-2 mb-4">
				{#if !account?.address}
					<div class="pl-4">
						<w3m-button label="Connect to Claim" />
					</div>
				{:else}
					<form
						method="POST"
						action="/claim?/postClaim"
						use:enhance={() => {
							return async ({ result, update }) => {
								/**
								 * @type {any}
								 */
								let res = result;
								loading = true;

								resMsg = res?.data?.result;
								await applyAction(result); // manually call applyAction to update `page.form`
								await update();
								loading = false;
							};
						}}
					>
						<input type="hidden" name="ledger_id" value={selectedChain?.ledger_id} />
						<TabGroup>
							<Tab bind:group={tabSet} name="tab1" value={0}>
								<span>Whitelisted</span>
							</Tab>
							<Tab bind:group={tabSet} name="tab2" value={1}>Custom Address</Tab>
							<!-- Tab Panels --->
							<svelte:fragment slot="panel">
								{#if tabSet === 0}
									<div class="mb-4 w-full tab">
										<input
											type="hidden"
											name="address"
											value={selectedAddress}
											placeholder="Select from whitelisted.."
										/>
										<AddressSelect bind:selected={selectedAddress} data={data?.whitelisted || []} />
									</div>
								{:else}
									<div class="mb-4 w-full tab">
										<input
											class="mb-4 w-full address"
											name="address"
											placeholder="Enter address.."
										/>
									</div>
								{/if}
							</svelte:fragment>
						</TabGroup>
						<button use:popup={popupHover} type="submit" class="btn variant-ghost-secondary w-full"
							>Claim</button
						>
						{#if loading}
							<div class="pt-2 status">Loading...</div>
						{/if}
						{#if resMsg}
							<div class="pt-2 status">{resMsg}</div>
						{/if}
					</form>
				{/if}
			</div>
			<img class="faucet-img" src="/faucet2.png" alt="faucet" />
			{#if account?.address}
				<div class="pl-10">
					<w3m-button label="Connect to Claim" />
				</div>
			{/if}
		</div>
	</div>
	<div class="card p-4 variant-filled-secondary" data-popup="popupHover">
		<p>Select a ledger to claim tokens from a faucet</p>
		<div class="arrow variant-filled-secondary" />
	</div>
</div>

<style>
	.status {
		width: 250px;
		color: #a8dfb0;
		font-size: 13px;
	}

	.tab {
		height: 100px;
		width: 380px;
	}

	.address {
		padding: 5px;
		border-radius: 5px;
		font-size: 12px;
		color: black;
	}

	.title {
		font-weight: 700;
		letter-spacing: 1.6px;
		font-size: 20px;
		line-height: 20px;
		color: #b2eafd;
	}

	.faucet-img {
		width: 250px;
		height: auto;
		margin-left: 58px;
		margin-bottom: 10px;
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
		height: 92vh;
	}

	.logo {
		width: 40px;
		height: 35px;
		margin: 0 7px;
	}
</style>
