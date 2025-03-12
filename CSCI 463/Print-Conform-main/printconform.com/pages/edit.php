<!-- PrintConform Edit PHP Code Version 1.0
Purpose: To allow for the user to edit photos.
Author: Isaac Barta 
Creation Date: 5-3-2024
Modification History:
    5-3-2024: Initial Version
    5-4-2024: Updated to include header.html and added an Upload Button
-->
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../styles/style.css"/>
        <link rel="icon" href="images/icon.png"/>
        <title>Edit - Print Conform</title>
    </head>
    <body>
        <?php include "../pages/header_login.php"; ?>
        <main>
            <div class="image_view">
                <div class="preview-img">
                    <img src="image-placeholder.svg" alt="preview-img">
                </div>
            </div>
            <div class="edit_panel">
                <h1 class="crop">Crop</h1>
                <div class="orientation">
                    <h2 class="rotate_flip">Rotate & Flip</h2>
                    <div class="options">
                        <button id="left">Left</button>
                        <button id="horizontal">Horizontal</button>
                        <button id="right">Right</button>
                        <button id="vertical">Vertical</button>
                    </div>
                </div>
                <h1>Filters</h1>
                <div class="filter">
                    <div class="options">
                        <button id="brightness" class="active">Brightness</button>
                        <button id="saturation">Saturation</button>
                        <button id="inversion">Inversion</button>
                        <button id="grayscale">Grayscale</button>
                    </div>
                    <div class="slider">
                        <div class="filter-info">
                            <p class="name">Brightness</p>
                            <p class="value">100%</p>
                        </div>
                        <input id="brightness" type="range" value="100" min="0" max="200">
                    </div>
                </div>
                <div class="controls">
                    <button class="reset-filter">Reset Filters</button>
                    <div class="row">
                        <input type="file" class="file-input" accept="image/*" hidden>
                        <button class="choose-img">Choose Image</button>
                        <button class="save-img">Save Image</button>
                        <button class="upload_img">Upload Image</button>
                    </div>
                </div>
            </div>
        </main>
        <script>
            const fileInput = document.querySelector(".file-input"),
            rotate_options = document.querySelectorAll(".orientation button"),
            filterOptions = document.querySelectorAll(".filter button"),
            filterName = document.querySelector(".filter-info .name"),
            filterValue = document.querySelector(".filter-info .value"),
            filterSlider = document.querySelector(".slider input"),
            previewImg = document.querySelector(".preview-img img"),
            resetFilterBtn = document.querySelector(".reset-filter"),
            chooseImgBtn = document.querySelector(".choose-img"),
            saveImgBtn = document.querySelector(".save-img");
            let brightness_slider = document.getElementById("brightness");
            let saturation_slider = document.getElementById("saturation");


            let saturation = "100", inversion = "0", grayscale = "0";
            let rotate = 0, flipHorizontal = 1, flipVertical = 1;

            const loadImage = () => {
                let file = fileInput.files[0];
                if(!file) return;
                previewImg.src = URL.createObjectURL(file);
                previewImg.addEventListener("load", () => {
                    resetFilterBtn.click();
                    document.querySelector(".container").classList.remove("disable");
                });
            }

            const applyFilter = () => {
                previewImg.style.transform = `rotate(${rotate}deg) scale(${flipHorizontal}, ${flipVertical})`;
                previewImg.style.filter = `brightness(${brightness}%) saturate(${saturation}%) invert(${inversion}%) grayscale(${grayscale}%)`;
            }

            filterOptions.forEach(option => {
                option.addEventListener("click", () => {
                    document.querySelector(".active").classList.remove("active");
                    option.classList.add("active");
                    filterName.innerText = option.innerText;

                    if(option.id === "brightness") {
                        filterSlider.max = "200";
                        filterSlider.value = brightness;
                        filterValue.innerText = `${brightness}%`;
                    } else if(option.id === "saturation") {
                        filterSlider.max = "200";
                        filterSlider.value = saturation;
                        filterValue.innerText = `${saturation}%`
                    } else if(option.id === "inversion") {
                        filterSlider.max = "100";
                        filterSlider.value = inversion;
                        filterValue.innerText = `${inversion}%`;
                    } else {
                        filterSlider.max = "100";
                        filterSlider.value = grayscale;
                        filterValue.innerText = `${grayscale}%`;
                    }
                });
            });

            const updateFilter = () => {
                filterValue.innerText = `${filterSlider.value}%`;
                const selectedFilter = document.querySelector(".filter .active");

                if(selectedFilter.id === "brightness") {
                    brightness = filterSlider.value;
                } else if(selectedFilter.id === "saturation") {
                    saturation = filterSlider.value;
                } else if(selectedFilter.id === "inversion") {
                    inversion = filterSlider.value;
                } else {
                    grayscale = filterSlider.value;
                }
                applyFilter();
            }

            rotate_options.forEach(option => {
                option.addEventListener("click", () => {
                    if(option.id === "left") {
                        rotate -= 90;
                    } else if(option.id === "right") {
                        rotate += 90;
                    } else if(option.id === "horizontal") {
                        flipHorizontal = flipHorizontal === 1 ? -1 : 1;
                    } else {
                        flipVertical = flipVertical === 1 ? -1 : 1;
                    }
                    applyFilter();
                });
            });

            const resetFilter = () => {
                brightness = "100"; saturation = "100"; inversion = "0"; grayscale = "0";
                rotate = 0; flipHorizontal = 1; flipVertical = 1;
                filterOptions[0].click();
                applyFilter();
            }

            const saveImage = () => {
                const canvas = document.createElement("canvas");
                const ctx = canvas.getContext("2d");
                canvas.width = previewImg.naturalWidth;
                canvas.height = previewImg.naturalHeight;
                
                ctx.filter = `brightness(${brightness}%) saturate(${saturation}%) invert(${inversion}%) grayscale(${grayscale}%)`;
                ctx.translate(canvas.width / 2, canvas.height / 2);
                if(rotate !== 0) {
                    ctx.rotate(rotate * Math.PI / 180);
                }
                ctx.scale(flipHorizontal, flipVertical);
                ctx.drawImage(previewImg, -canvas.width / 2, -canvas.height / 2, canvas.width, canvas.height);
                
                const link = document.createElement("a");
                link.download = "image.jpg";
                link.href = canvas.toDataURL();
                link.click();
            }

            filterSlider.addEventListener("input", updateFilter);
            resetFilterBtn.addEventListener("click", resetFilter);
            saveImgBtn.addEventListener("click", saveImage);
            fileInput.addEventListener("change", loadImage);
            chooseImgBtn.addEventListener("click", () => fileInput.click());
        </script>
    </body>
    <style>
        :root {
            --navbar_height: 56px;
            --pcpurple: rgb(142, 127, 204);
            --gray0: rgb(10, 10, 10);
            --gray1: rgb(30, 30, 30);
            --gray2: rgb(50, 50, 50);
            --gray3: rgb(70, 70, 70);
        }

        main {
            display: flex;
            justify-content: space-between;
        }

        .image_view {
            height: calc(100vh - var(--navbar_height));
            width: calc(100% - 400px);
            transform: translateY(var(--navbar_height));
        }

        .preview-img {
            flex-grow: 1;
            overflow: hidden;
            margin: 20px;
            border-radius: 5px;
            align-items: center;
            justify-content: center;
        }

        .preview-img img {
            max-width: 100%;
            max-height: calc(100vh - var(--navbar_height) - 40px);
            width: 100%;
            height: 100%;
            object-fit: contain;
        }

        .edit_panel{
            background-color: var(--gray2);
            height: calc(100vh - var(--navbar_height) - 40px);
            width: 400px;
            transform: translateY(calc(var(--navbar_height) + 20px));
            border-radius: 25px 0px 0px 25px;
            overflow: hidden;
        }

        .edit_panel h1 {
            color: white;
            margin-left: 20px;
        }

        .edit_panel h2 {
            color: white;
            margin-left: 20px;
        }

        .edit_panel .crop {
            margin-top: 20px;
        }

        .edit_panel .rotate_flip {
            margin-top: 10px;
        }

        .edit_panel .options {
            width: 100%;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            padding: 10px 20px;
            gap: 10px;
        }

        .edit_panel .options button {
            height: 40px;
            width: 170px;
            background-color: var(--pcpurple);
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-weight: bold;
            font-size: 16px;
            color: white;
            overflow: hidden;
        }

        .edit_panel .options button:hover {
            background-color: white;
            color: var(--pcpurple);
            scale: 1.05;
        }

        .edit_panel .options button:active {
            scale: 0.95;
        }

        .filter button.active{
            background-color: white;
            color: var(--pcpurple);
        }

        .filter .slider{
            margin: 10px 20px;
        }

        .filter .slider .filter-info{
            display: flex;
            color: white;
            font-size: 16px;
            justify-content: space-between;
        }

        .filter .slider input {
            width: 100%;
            height: 5px;
            accent-color: var(--pcpurple);
        }

        .edit_panel .controls {
            display: flex;
            flex-direction: column;
            height: 480px;
        }

        .edit_panel .controls button {
            height: 50px;
            width: 360px;
            background-color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-weight: bold;
            font-size: 16px;
            color: var(--pcpurple);
            overflow: hidden;
            margin-left: 20px;
            margin-top: 10px;
        }

        .edit_panel .controls button:hover {
            background-color: var(--pcpurple);
            color: white;
            scale: 1.05;
        }

        .edit_panel .controls button:active {
            scale: 0.95;
        }

        .edit_panel .controls .upload_img {
            height: 50px;
            width: 360px;
            background-color: var(--pcpurple);
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-weight: bold;
            font-size: 16px;
            color: white;
            overflow: hidden;
            margin-left: 20px;
            margin-top: 200px;
        }

        .edit_panel .controls .upload_img:hover {
            background-color: white;
            color: var(--pcpurple);
            scale: 1.05;
        }

        .edit_panel .controls .upload_img:active {
            scale: 0.95;
        }
    </style>
</html>