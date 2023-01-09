<template>
    <div class="backdrop">
        <div class="modal">
            <p>modal contant</p>
        </div>
    </div>
</template>

<style>
.modal
{

    width: 400px;
    background-color: white;
    border-radius: 10px;
    padding: 20px;
    margin: 100px auto;


}

.backdrop
{
    top: 0;
    position: fixed;
    background-color: rgba(0,0,0,0.5);
    width: 100%;
    height: 100%;
}


</style>