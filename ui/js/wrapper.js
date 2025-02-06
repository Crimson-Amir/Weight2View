export const findItem = async(weight, id) => 
{
    try 
    {
        const req = await fetch(import.meta.env.VITE_DB_URL+"find_first_item", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "item_id": id,
                "weight_in_gram": parseFloat(weight)
            })
        })

        const res = await req.json()

        return res.svg_plot
    } 
    catch (error) {
        console.error(error)
    }
}