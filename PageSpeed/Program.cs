using System;
using System.Web;
using System.Net;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace PageSpeedApi
{
    class Program
    {
        static void Main(string[] args)
        {
            PageSpeed ps = new PageSpeed();

            //Console.WriteLine("Enter domain: ");
            string url = "https://www.performance-law.com";

            // https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url=https%3a%2f%2fwww.performance-law.com&strategy=mobile&key=AIzaSyDJNu6pW7kifKiVssTdMlyad-hUc3stgOg

            string googlePageSpeedApiUrl = "https://www.googleapis.com/pagespeedonline/v4/runPagespeed";

            string pagespeedUrl = googlePageSpeedApiUrl +
            "?url=" + HttpUtility.UrlEncode(url) +
            "&strategy=mobile&key=" + ps.apiKey;

            string content = string.Empty;
            WebResponse response = null;
            WebRequest wr = WebRequest.Create(pagespeedUrl);
            wr.Method = "GET";
            response = wr.GetResponse();

            using (StreamReader sr = new StreamReader(response.GetResponseStream()))
            {
                content = sr.ReadToEnd();
                sr.Close();
            }

            JObject json = JObject.Parse(content);

            // var json = JsonConvert.DeserializeObject<PageSpeedData>(content);

            var value = json["formattedResults"]["ruleResults"]["OptimizeImages"]["urlBlocks"][0]["urls"];

            foreach (var item in value)
            {
                Console.WriteLine(item["result"]["args"][0]["value"]);
            }

            Console.ReadLine();

        }
    }
}
