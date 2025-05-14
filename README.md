# Matching the Stitch
Repository for models, data, and code associated with the project Matching the Stitch.

This repository will be consistently updated to increase its utility as a toolkit for designing, digitally restoring, and making tactile reproductions of embroidered goods. All models that this projects makes use of are open source. We have made extensive use of the open source software [inkscape](https://inkscape.org/) and its add-on [ink/stitch](https://inkstitch.org/), [DepthAnything_V2](https://depth-anything-v2.github.io/), [comfyui](https://www.comfy.org/), [stable diffusion](https://stability.ai/) and [flux](https://github.com/black-forest-labs/flux) models along with named fine-tunes, [SegmentAnything2](https://ai.meta.com/sam2/), and resnet50.

## LoRAs

Loras trained for stitch types using multiple popular open source models. Download the samples and drag the .png into comfyui to see the full workflow used to create the grid. Some LoRAs are split into multiple zipped files to come under the upload file size limit.

More stitch types will be uploaded when they are created. If there is a specific stitch type that you'd like ot see added to the collection, please contact me.

### Samples

These samples are all illustrated using different prompts, which are visible if you drop the .png into a comfyui workflow. Better results are likely possible with different priompts (e.g. by including the word "embroidery")

#### Flux
![flux](LoRAs/Samples/flux.png)

#### Flex
![flex](LoRAs/Samples/flex.png)

#### Juggernaut XI (XL)
![juggernaut](LoRAs/Samples/juggernaut.png)

#### SDXL base
![sdxl](LoRAs/Samples/sdxl.png)

#### SD1.5
![sd15](LoRAs/Samples/sd15.png)

#### RealVis 4.0 (XL)
![realvis](LoRAs/Samples/realvis.png)

#### SD3.5 Large
![sd35large](LoRAs/Samples/sdx35large.png)

#### SD3.5 Medium
![sd35med](LoRAs/Samples/sdx35medium.png)

#### SD3.5 Medium including "embroidery" in prompt
![sd35medemb](LoRAs/Samples/sdx35medium_embroidery.png)


## Classifiers

The neural net "stitch-matcher" was trained across scales to identify stitch types from colour photos. There is a black and white counterpart which has a similar success rate at identifying stitch type.

We plan to update this with neural nets trained on roughness, normals, and depth maps, to increase the power of our classifier.

This is used as part of the script ...py to output a colour-coded png file where each colour represents a distinct stitch type.

## Ink-stitch

This includes a script that converts the colour coded stutch type to a vector file compatible with inkscape. It is simple to convert this to an embroidery machine file with inkstitch, or to a machining file appropriate for another production mechanism with an artificial/added texture.
