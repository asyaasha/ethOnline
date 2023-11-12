<script>
	export let selected = '';
	/**
	 * @type {any}
	 */
	export let data;
</script>

<select bind:value={selected}>
	<option value="" disabled selected>Select Address..</option>
	{#each data as option (option)}
		<option value={option}>{option}</option>
	{/each}
</select>

<style>
	select {
		padding: 4px;
		border: 0.8px solid #ddddddb7;
		border-radius: 4px;
		font-size: 14px;
		width: 100%;
		background: rgb(0, 5, 8);
		color: rgb(251, 251, 251);
		font-weight: 400;
	}
</style>
